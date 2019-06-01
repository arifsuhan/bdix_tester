
function check() 
{ 
    var connection = document.getElementById('check_connection');

    if(navigator.onLine) 
    {
        connection.innerHTML = 'Internet Connection is on';
    }
    else
    {
        connection.innerHTML = 'System is out of Internet';
    }
}


function pingCheck(address)
{
	var p = new Ping();
    var msg = "";

	p.ping("https://"+ address, function(err, time) {

      if(err === "error")
      {
        msg = "Ping error";
      }
      else
      {
        msg = "Ping in "+time+" miliseconds ";
      }

      document.getElementById("timeCheck").innerHTML = msg;

	});
}