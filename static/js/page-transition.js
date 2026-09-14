(function () {
  var transitionMs = 240;

  window.addEventListener("pageshow", function () {
    document.body.classList.remove("page-leaving");
  });

  document.addEventListener("click", function (event) {
    var link = event.target.closest("a[href]");

    if (!link || event.defaultPrevented || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }

    if (link.target && link.target !== "_self") {
      return;
    }

    var href = link.getAttribute("href");
    var url = new URL(link.href, window.location.href);
    var isSameOrigin = url.origin === window.location.origin;
    var isCurrentPage = url.pathname === window.location.pathname && url.search === window.location.search && !url.hash;
    var isSamePageHash = url.pathname === window.location.pathname && url.search === window.location.search && url.hash;

    if (href === "#" || !isSameOrigin || isCurrentPage || isSamePageHash || url.protocol === "mailto:" || url.protocol === "tel:") {
      return;
    }

    event.preventDefault();
    document.body.classList.add("page-leaving");

    window.setTimeout(function () {
      window.location.href = url.href;
    }, transitionMs);
  });
})();
