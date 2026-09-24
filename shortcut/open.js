// 페이지 언어(<html lang>)에 맞는 단축어를 단축어 앱으로 연다.
// 단축어 iCloud ID는 links.json 한 곳에서 관리한다(알림함 앱도 같은 파일을 읽는다).
(function () {
  var lang = document.documentElement.lang === "en" ? "en" : "ko";
  var isApple = /iPhone|iPad|iPod|Macintosh/.test(navigator.userAgent);

  fetch("../../links.json", { cache: "no-store" })
    .then(function (res) { return res.json(); })
    .then(function (links) {
      var id = links[lang];
      // iCloud 공유 페이지의 'Get Shortcut' 버튼과 같은 방식
      var appURL = "workflow://shortcuts/" + encodeURIComponent(id);
      document.getElementById("open").href = appURL;
      document.getElementById("web").href = "https://www.icloud.com/shortcuts/" + id;
      if (isApple) window.location.href = appURL;
    })
    .finally(function () {
      // 앱이 안 열렸을 때(확인창 취소, 다른 기기 등) 직접 누를 수 있게 버튼을 보여준다.
      setTimeout(function () { document.body.classList.add("fallback"); }, isApple ? 2500 : 0);
    });
})();
