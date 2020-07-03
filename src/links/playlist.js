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
        console.log(message);
    })
}