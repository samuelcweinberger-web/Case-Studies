const header = document.querySelector(".site-header");
if (header) {
  const onScroll = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (prefersReducedMotion) {
  document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-visible"));
} else {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
  );

  document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
}

// Theme toggle — the inline <head> script sets data-theme pre-paint; this
// just flips it and persists the choice.
document.querySelectorAll("[data-theme-toggle]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const next =
      document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("theme", next);
    } catch (e) {
      /* private mode */
    }
  });
});

// Industry filter pills on the case-studies index.
document.querySelectorAll("[data-case-filters]").forEach((bar) => {
  const pills = Array.from(bar.querySelectorAll(".filter-pill"));
  const groups = Array.from(document.querySelectorAll(".company-group[data-industry]"));
  pills.forEach((pill) => {
    pill.addEventListener("click", () => {
      const filter = pill.dataset.filter;
      pills.forEach((p) => {
        const active = p === pill;
        p.classList.toggle("is-active", active);
        p.setAttribute("aria-pressed", String(active));
      });
      groups.forEach((group) => {
        const show = filter === "all" || group.dataset.industry === filter;
        group.classList.remove("is-filter-in");
        group.classList.toggle("is-filtered-out", !show);
        if (show) {
          group.classList.add("is-visible");
          void group.offsetWidth;
          group.classList.add("is-filter-in");
        }
      });
    });
  });
});

// Sticky TOC scroll-spy on case pages.
document.querySelectorAll("[data-case-toc]").forEach((toc) => {
  const links = Array.from(toc.querySelectorAll('a[href^="#"]'));
  const sections = links
    .map((link) => document.getElementById(link.getAttribute("href").slice(1)))
    .filter(Boolean);
  if (!sections.length) return;

  const setCurrent = (id) => {
    links.forEach((link) =>
      link.classList.toggle("is-current", link.getAttribute("href") === `#${id}`)
    );
  };

  const spy = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible.length) setCurrent(visible[0].target.id);
    },
    { rootMargin: "-20% 0px -60% 0px", threshold: 0 }
  );

  sections.forEach((section) => spy.observe(section));
  setCurrent(sections[0].id);
});

document.querySelectorAll("[data-video-cta]").forEach((btn) => {
  const frame = btn.closest(".video-loop-frame");
  const video = frame && frame.querySelector("video");
  if (!video) return;
  btn.addEventListener("click", () => {
    video.currentTime = 0;
    const playback = video.play();
    if (playback && typeof playback.catch === "function") playback.catch(() => {});
    if (typeof video.requestFullscreen === "function") {
      video.requestFullscreen().catch(() => {});
    } else if (typeof video.webkitRequestFullscreen === "function") {
      video.webkitRequestFullscreen();
    } else if (typeof video.webkitEnterFullscreen === "function") {
      video.webkitEnterFullscreen();
    }
  });
});

document.querySelectorAll("[data-video-click]").forEach((frame) => {
  const video = frame.querySelector("video");
  const btn = frame.querySelector(".video-click-cta");
  if (!video || !btn) return;

  const enterFullscreen = () => {
    if (typeof video.requestFullscreen === "function") {
      return video.requestFullscreen();
    }
    if (typeof video.webkitRequestFullscreen === "function") {
      video.webkitRequestFullscreen();
      return Promise.resolve();
    }
    if (typeof video.webkitEnterFullscreen === "function") {
      video.webkitEnterFullscreen();
      return Promise.resolve();
    }
    return Promise.resolve();
  };

  const resetToPoster = () => {
    frame.classList.remove("is-playing");
    video.pause();
    video.currentTime = 0;
    video.hidden = true;
    video.removeAttribute("controls");
  };

  const playVideo = () => {
    frame.classList.add("is-playing");
    video.hidden = false;
    video.muted = false;
    video.controls = true;
    video.currentTime = 0;
    const playback = video.play();
    if (playback && typeof playback.catch === "function") {
      playback.catch(() => {});
    }
    enterFullscreen().catch(() => {});
  };

  btn.addEventListener("click", (e) => {
    e.stopPropagation();
    playVideo();
  });
  frame.addEventListener("click", (e) => {
    if (e.target === btn || btn.contains(e.target)) return;
    if (!frame.classList.contains("is-playing")) playVideo();
  });

  video.addEventListener("ended", resetToPoster);
  document.addEventListener("fullscreenchange", () => {
    if (!document.fullscreenElement && frame.classList.contains("is-playing")) {
      resetToPoster();
    }
  });
  document.addEventListener("webkitfullscreenchange", () => {
    if (!document.webkitFullscreenElement && frame.classList.contains("is-playing")) {
      resetToPoster();
    }
  });
});

document.querySelectorAll("[data-print]").forEach((btn) => {
  btn.addEventListener("click", () => window.print());
});

// Per-product case carousels on the case-studies index. The track scrolls
// natively (works with JS off); this just wires the prev/next controls and
// keeps their state in sync with scroll position.
document.querySelectorAll("[data-pcarousel]").forEach((carousel) => {
  const track = carousel.querySelector("[data-pcar-track]");
  const prev = carousel.querySelector("[data-pcar-prev]");
  const next = carousel.querySelector("[data-pcar-next]");
  if (!track) return;

  const step = () => {
    const card = track.querySelector(".case-card");
    const gap = parseFloat(getComputedStyle(track).columnGap || "0") || 20;
    const cardW = card ? card.getBoundingClientRect().width + gap : track.clientWidth * 0.8;
    return Math.max(cardW, track.clientWidth * 0.6);
  };

  const update = () => {
    const overflowing = track.scrollWidth - track.clientWidth > 4;
    carousel.classList.toggle("has-overflow", overflowing);
    if (!overflowing) {
      if (prev) prev.hidden = true;
      if (next) next.hidden = true;
      return;
    }
    const maxScroll = track.scrollWidth - track.clientWidth;
    const atStart = track.scrollLeft <= 2;
    const atEnd = track.scrollLeft >= maxScroll - 2;
    if (prev) {
      prev.hidden = false;
      prev.disabled = atStart;
    }
    if (next) {
      next.hidden = false;
      next.disabled = atEnd;
    }
  };

  if (prev) prev.addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
  if (next) next.addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));

  track.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      e.preventDefault();
      track.scrollBy({ left: step(), behavior: "smooth" });
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      track.scrollBy({ left: -step(), behavior: "smooth" });
    }
  });

  track.addEventListener("scroll", () => {
    window.requestAnimationFrame(update);
  }, { passive: true });
  window.addEventListener("resize", () => window.requestAnimationFrame(update), { passive: true });
  update();
});

// Cinematic hero background — the sizzle-reel <video> ships with
// preload="none" and a poster, so no video bytes move until this decides
// playback is appropriate: wide viewport, motion allowed, no data-saver.
// Small screens and reduced-motion users just keep the poster frame.
const heroVideo = document.querySelector("[data-hero-video]");
if (heroVideo) {
  const wideViewport = window.matchMedia("(min-width: 780px)");
  const saveData = navigator.connection && navigator.connection.saveData;

  const startHeroVideo = () => {
    if (heroVideo.dataset.started) return;
    heroVideo.dataset.started = "true";
    heroVideo.muted = true;
    heroVideo.preload = "auto";
    const playback = heroVideo.play();
    if (playback && typeof playback.catch === "function") playback.catch(() => {});
  };

  heroVideo.addEventListener(
    "playing",
    () => heroVideo.classList.add("is-playing"),
    { once: true }
  );

  if (!prefersReducedMotion && !saveData) {
    if (wideViewport.matches) {
      startHeroVideo();
    } else if (typeof wideViewport.addEventListener === "function") {
      wideViewport.addEventListener("change", (e) => {
        if (e.matches) startHeroVideo();
      });
    }

    // Don't keep decoding video the visitor has scrolled past.
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (!heroVideo.dataset.started) return;
            if (entry.isIntersecting) {
              const playback = heroVideo.play();
              if (playback && typeof playback.catch === "function") playback.catch(() => {});
            } else {
              heroVideo.pause();
            }
          });
        },
        { threshold: 0.05 }
      ).observe(heroVideo);
    }
  }
}

// "Choose your path" filter over the typographic case index on the home page.
document.querySelectorAll("[data-case-index]").forEach((list) => {
  const rows = Array.from(list.querySelectorAll(".idx-row"));
  const links = Array.from(document.querySelectorAll(".path-link"));
  if (!links.length) return;
  links.forEach((link) => {
    link.addEventListener("click", () => {
      const path = link.dataset.path;
      links.forEach((l) => {
        const active = l === link;
        l.classList.toggle("is-active", active);
        l.setAttribute("aria-pressed", String(active));
      });
      rows.forEach((row) => {
        const show = path === "all" || row.dataset.industry === path;
        row.classList.toggle("is-hidden", !show);
        if (show) row.classList.add("is-visible");
      });
    });
  });
});

document.querySelectorAll("[data-carousel]").forEach((carousel) => {
  const slides = Array.from(carousel.querySelectorAll(".carousel-slide"));
  if (!slides.length) return;
  const prev = carousel.querySelector("[data-carousel-prev]");
  const next = carousel.querySelector("[data-carousel-next]");
  const current = carousel.querySelector("[data-carousel-current]");
  const caption = carousel.querySelector("[data-carousel-caption]");
  let index = 0;
  const show = (n) => {
    index = (n + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      const depth = (i - index + slides.length) % slides.length;
      slide.dataset.depth = String(depth);
      slide.classList.toggle("is-active", depth === 0);
    });
    if (current) current.textContent = String(index + 1);
    if (caption) caption.textContent = slides[index].dataset.caption || "";
  };
  if (prev) prev.addEventListener("click", () => show(index - 1));
  if (next) next.addEventListener("click", () => show(index + 1));
  show(0);
});
