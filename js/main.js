/* ==========================================================================
   Lakeview UMC - Ministry Partner Page
   Vanilla JS only: nav toggle, scroll-reveal, direct-giving panel,
   and the PayMongo link configuration.
   ========================================================================== */

(function () {
  "use strict";

  /* ------------------------------------------------------------------
   * PAYMONGO LINKS - EDIT HERE
   * Replace each placeholder string with the real PayMongo-hosted
   * payment URL once it has been created in the PayMongo dashboard.
   * See README.md -> "Where to add the real PayMongo links".
   * ------------------------------------------------------------------ */
  var PAYMONGO_LINKS = {
    onetime: "https://pm.link/PAYMONGO_LINK_ONETIME",   // [FILL IN] One-Time Gift
    monthly: "https://pm.link/PAYMONGO_LINK_MONTHLY",   // [FILL IN] Monthly Partner pledge
    lovegift: "https://pm.link/PAYMONGO_LINK_LOVEGIFT"  // [FILL IN] Love Gift
  };

  document.querySelectorAll(".partner-link").forEach(function (link) {
    var key = link.getAttribute("data-link-key");
    if (PAYMONGO_LINKS[key]) {
      link.setAttribute("href", PAYMONGO_LINKS[key]);
    }
  });

  /* ------------------------------------------------------------------
   * Mobile nav toggle
   * ------------------------------------------------------------------ */
  var navToggle = document.getElementById("navToggle");
  var primaryNav = document.getElementById("primaryNav");

  if (navToggle && primaryNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = primaryNav.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    primaryNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        primaryNav.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ------------------------------------------------------------------
   * Direct giving (GCash / bank transfer) expandable panel
   * ------------------------------------------------------------------ */
  var directToggle = document.getElementById("directGivingToggle");
  var directPanel = document.getElementById("directGivingPanel");

  if (directToggle && directPanel) {
    directToggle.addEventListener("click", function () {
      var isOpen = directToggle.getAttribute("aria-expanded") === "true";
      directToggle.setAttribute("aria-expanded", String(!isOpen));
      directPanel.hidden = isOpen;
    });
  }

  /* ------------------------------------------------------------------
   * Scroll reveal (progressive enhancement; content is visible
   * without JS, see .reveal default state in styles.css)
   * ------------------------------------------------------------------ */
  document.documentElement.classList.add("js-enabled");

  if ("IntersectionObserver" in window) {
    var revealEls = document.querySelectorAll(".reveal");
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      // threshold 0: fire as soon as any part of the element enters the
      // viewport. A percentage threshold (e.g. 0.12) is unreliable here
      // because some sections (the ministries grid, the budget table) are
      // taller than the viewport, so that percentage of their own area
      // can never become visible at once - the section would stay at
      // opacity 0 forever.
      { threshold: 0, rootMargin: "0px 0px -10% 0px" }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) {
      el.classList.add("is-visible");
    });
  }
})();
