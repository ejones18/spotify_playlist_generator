function gen_playlist() {
    let {PythonShell} = require('python-shell');
    var path = require ('path')
    
    var artist = document.getElementById('artist').value
    var track = document.getElementById('track').value
    
    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        args : ["-a", artist, "-t", track]
    }
    
    var playlist = new PythonShell('playlist_recommendations.py', options);
    
    playlist.on('message', function(message) {
        if (message === "Sorry, an error occurred. Please try again."){
            alert(message)
        }
        else{
            document.getElementById("submitButton").remove();
            document.getElementById("artist").remove();
            document.getElementById("track").remove();
            
            var playlist_paragraph = document.createElement("p");
            var playlist_text = document.createTextNode(message);
            playlist_paragraph.appendChild(playlist_text);
            var element_to_append = document.getElementById("container");
            element_to_append.appendChild(playlist_paragraph);
        }
    })
};