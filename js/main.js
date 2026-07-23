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
