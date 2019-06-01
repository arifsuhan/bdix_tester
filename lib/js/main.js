
function check() 
{ 
    var connection = document.getElementById('check_connection');

    if(navigator.onLine) 
    {
        connection.innerHTML = 'Internet Connection is on';
        connection.style.color = '#4492ff';
    }
    else
    {
        connection.innerHTML = 'System is out of Internet';
        connection.style.color = '#ff2b2b';
    }
}


function wayOne(address)
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



function pingCheck()
{
    var address = document.getElementById('addr').value;
    wayOne(address);
}