// Per-section header brand.
//
// The site shares one header (Material renders `site_name` in the top-left
// corner on every page). On the Hecate Admin pages we want that corner to read
// "Hecate · Admin" instead of plain "Hecate", so the section is obvious at a
// glance — while the capture-app pages keep saying "Hecate".
//
// `navigation.instant` is intentionally disabled (see mkdocs.yml), so every page
// is a full load and a one-shot DOMContentLoaded handler is sufficient. The path
// check matches every locale (/hecate-admin/, /de/hecate-admin/, …).
(function () {
  function applyBrand() {
    var isAdmin = location.pathname.indexOf("/hecate-admin/") !== -1;
    // The first `.md-header__topic` holds the site name; the second (with
    // data-md-component="header-topic") is the scrolled page title — leave it.
    var brand = document.querySelector(
      ".md-header__title .md-header__topic .md-ellipsis"
    );
    if (brand) brand.textContent = isAdmin ? "Hecate · Admin" : "Hecate";
  }
  document.addEventListener("DOMContentLoaded", applyBrand);
})();
