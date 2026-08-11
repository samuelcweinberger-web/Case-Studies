// Case-study passcode gate. The pre-paint inline script in each case page's
// <head> decides whether this visit is locked (data-case-locked on <html>):
// the first case a visitor opens is free forever, any other case is gated
// until the passcode is entered once. This is a client-side courtesy gate,
// not security — the content is still in the HTML source.
(function () {
  var root = document.documentElement;
  var gate = document.querySelector("[data-case-gate]");
  if (!gate) return;

  var form = gate.querySelector("[data-gate-form]");
  var input = gate.querySelector("#case-gate-code");
  var error = gate.querySelector("[data-gate-error]");
  if (!form || !input || !error) return;

  // Lightly obfuscated so the passcode doesn't turn up with a trivial
  // find-in-page over the source. Obfuscation, not security.
  var expected = atob("RmRRZnRSc0UtMTU0MzIz");

  var isLocked = function () {
    return root.hasAttribute("data-case-locked");
  };

  var unlock = function () {
    try {
      localStorage.setItem("caseGateUnlocked", "true");
    } catch (e) {
      /* private mode — unlock still applies for this page view */
    }
    root.removeAttribute("data-case-locked");
    document.removeEventListener("keydown", onKeydown, true);
    var heading = document.querySelector("main h1");
    if (heading) {
      heading.setAttribute("tabindex", "-1");
      heading.focus();
    }
  };

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if ((input.value || "").trim() === expected) {
      error.hidden = true;
      unlock();
    } else {
      error.hidden = false;
      input.setAttribute("aria-invalid", "true");
      input.focus();
      input.select();
    }
  });

  input.addEventListener("input", function () {
    error.hidden = true;
    input.removeAttribute("aria-invalid");
  });

  // While locked: keep focus inside the dialog and swallow Escape — the
  // gate should genuinely block reading, not politely step aside.
  var onKeydown = function (e) {
    if (!isLocked()) return;
    if (e.key === "Escape") {
      e.preventDefault();
      return;
    }
    if (e.key !== "Tab") return;
    var focusables = gate.querySelectorAll("input, button, a[href]");
    if (!focusables.length) return;
    var first = focusables[0];
    var last = focusables[focusables.length - 1];
    if (!gate.contains(document.activeElement)) {
      e.preventDefault();
      input.focus();
    } else if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  };

  if (isLocked()) {
    document.addEventListener("keydown", onKeydown, true);
    window.setTimeout(function () {
      if (isLocked()) input.focus();
    }, 0);
  }
})();
