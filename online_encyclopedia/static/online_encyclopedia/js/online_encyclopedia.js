// tinymce.PluginManager.add('autolink_terms', function(editor) {
//     editor.on('init', function() {
//         fetch('online_encyclopedia/get-terms/')
//             .then(response => response.json())
//             .then(data => {
//                 editor.on('input', function() {
//                     let content = editor.getContent();
//                     data.terms.forEach(term => {
//                         let regex = new RegExp('\\b' + term.title + '\\b', 'gi');
//                         content = content.replace(regex, `<a href="/terms/${term.slug}/">${term.title}</a>`);
//                     });
//                     editor.setContent(content);
//                 });
//             });
//     });
// });