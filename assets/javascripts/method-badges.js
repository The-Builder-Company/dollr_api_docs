/**
 * HTTP Method Badges
 * Automatically wraps HTTP method names (GET, POST, PUT, DELETE, PATCH)
 * in colored badge spans inside ```http code blocks.
 *
 * Uses Material for MkDocs' document$ observable so it fires correctly
 * on both initial page load and instant navigation.
 */
document$.subscribe(function () {
  document.querySelectorAll("code.language-http").forEach(function (block) {
    const methods = ["DELETE", "PATCH", "POST", "PUT", "GET"];
    for (const method of methods) {
      if (block.textContent.trimStart().startsWith(method)) {
        block.innerHTML = block.innerHTML.replace(
          new RegExp("^(\\s*)" + method),
          '$1<span class="method-badge method-' + method.toLowerCase() + '">' + method + "</span>"
        );
        break;
      }
    }
  });
});
