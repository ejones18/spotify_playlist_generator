const {app, BrowserWindow, Menu} = require('electron');
const path = require('path')
const url = require('url')
const template = [
    {
        label: app.name,
        submenu: [
            { role: 'about'},
            { type: 'separator'},
            { role: 'quit'}
        ]
    }
]

const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)
let win;

function create_window(){
    win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });
    //win.webContents.openDevTools()
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'src/templates/index.html'),
        protocol: 'file:',
        slashes: true
    }));
}

app.on('ready', create_window); 

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin'){
        app.quit();
    }
});