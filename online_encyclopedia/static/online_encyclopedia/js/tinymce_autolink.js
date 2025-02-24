document.addEventListener("DOMContentLoaded", function() {
    if (typeof tinymce === 'undefined') {
        console.error("TinyMCE is not loaded!");
        return;
    }

    tinymce.init({
        selector: 'textarea',
        plugins: 'autolink_terms',
        toolbar: 'bold italic underline | link',
        menubar: false,
        content_style: `
            a.encyclopedia-term { color: blue; text-decoration: underline; cursor: pointer; }
        `,
    });
});


    tinymce.PluginManager.add('autolink_terms', function(editor) {
        editor.on('init', function() {
            fetch('online_encyclopedia/get-terms/')
                .then(response => response.json())
                .then(data => {
                    editor.on('input', function() {
                        let content = editor.getContent();
                        data.terms.forEach(term => {
                            let regex = new RegExp('\\b' + term.title + '\\b', 'gi');
                            content = content.replace(regex, `<a href=" /online_encyclopedia/terms/${term.slug}/" class="encyclopedia-term">${term.title}</a>`);
                        });
                        editor.setContent(content);
                    });
                });
        });
    });




