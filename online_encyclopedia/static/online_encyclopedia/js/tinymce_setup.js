document.addEventListener("DOMContentLoaded", function() {
    tinymce.init({
        selector: 'textarea', // დარწმუნდი, რომ სწორი სელექტორია
        plugins: 'autolink_terms',
        toolbar: 'bold italic underline | link',
        menubar: false,
        content_style: `
            a.encyclopedia-term { color: blue; text-decoration: underline; cursor: pointer; }
        `,
        setup: function(editor) {
            editor.on('init', function() {
                let script = document.createElement("script");
                script.src = "/static/online_encyclopedia/js/tinymce_autolink.js";
                document.body.appendChild(script);
            });
        }
    });
});