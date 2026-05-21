/**
 * Open the Mintlify docs assistant on each page load unless the reader closed it
 * this session (sessionStorage). Requires Assistant enabled in Mintlify Dashboard.
 */
(function () {
  var DISMISS_KEY = "dollr-docs-assistant-dismissed";

  function tryOpenAssistant() {
    if (sessionStorage.getItem(DISMISS_KEY) === "1") return;

    var params = new URL(window.location.href).searchParams;
    if (params.get("assistant") !== "open") {
      params.set("assistant", "open");
      var next = window.location.pathname + "?" + params.toString() + window.location.hash;
      window.history.replaceState({}, "", next);
    }

    var entry = document.getElementById("assistant-entry");
    if (entry) entry.click();
  }

  function watchDismiss() {
    var root = document.documentElement;
    if (!root || !window.MutationObserver) return;

    var observer = new MutationObserver(function () {
      if (root.getAttribute("data-assistant-state") === "closed") {
        sessionStorage.setItem(DISMISS_KEY, "1");
      }
    });

    observer.observe(root, {
      attributes: true,
      attributeFilter: ["data-assistant-state"],
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      tryOpenAssistant();
      watchDismiss();
    });
  } else {
    tryOpenAssistant();
    watchDismiss();
  }
})();
