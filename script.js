function getPlatform() {
    var userAgent = window.navigator.userAgent;
    if (userAgent.includes("Windows NT")) {
        return "Windows";
    } else if (userAgent.includes("Mac OS X")) {
        return "MacOS";
    } else {
        return "Unknown";
    }
}

document.getElementById('version').addEventListener('click', function() {
    var platform = getPlatform();
    var downloadLink;
    if (platform === "Windows") {
        downloadLink = "https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases/download/NPTE1.0.6.0/NPTESetup1.0.6.0.exe";
    } else if (platform === "MacOS") {
        downloadLink = "https://github.com/Anakin-bb8/Nuitka-GUI-NPTE/releases/download/NPTE1.0.6.0/NPTEInstaller1.2.pkg";
    } else {
        alert("Your platform isn't supported.");
        return;
    }
    window.location.href = downloadLink;
});


