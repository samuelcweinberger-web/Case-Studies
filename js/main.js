const header = document.querySelector(".site-header");
if (header) {
  const onScroll = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
}

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

document.querySelectorAll("[data-carousel]").forEach((carousel) => {
  const slides = Array.from(carousel.querySelectorAll(".carousel-slide"));
  if (slides.length < 2) return;
  const prev = carousel.querySelector("[data-carousel-prev]");
  const next = carousel.querySelector("[data-carousel-next]");
  const current = carousel.querySelector("[data-carousel-current]");
  const caption = carousel.querySelector("[data-carousel-caption]");
  let index = 0;
  const show = (n) => {
    index = (n + slides.length) % slides.length;
    slides.forEach((slide, i) => slide.classList.toggle("is-active", i === index));
    if (current) current.textContent = String(index + 1);
    if (caption) caption.textContent = slides[index].dataset.caption || "";
  };
  if (prev) prev.addEventListener("click", () => show(index - 1));
  if (next) next.addEventListener("click", () => show(index + 1));
  show(0);
});
