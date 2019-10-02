function reloadGraph() {
   var now = new Date();

   document.images['kamerakep'].src = 'http://cam.idokep.hu/kamera.php?user=honfyrk&' + now.getTime();

   // Start new timer (1 min)
   timeoutID = setTimeout('reloadGraph()', 5000);
}
