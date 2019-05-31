function check_ping () {

	ping -q -c1 $1 > /dev/null
	 
	if [ $? -eq 0 ]
	then
		echo "(!)" $1 "is connected"
	else
		echo "(x)" $1 "is not connected"
	fi

}

function series_ip(){

	for ip in `seq 1 $1`
	do
	  check_ping 192.168.0.$ip
	done
}


function main(){

	echo "\n"
	series_ip $1
	echo "\n"

}

#range_v=20
#main $range_v

fileName="bdix_ip.csv"

while read -r col1 col2
do
    #echo $col1			#skipping commma	
    check_ping $col1
done < $fileName


function fromFileCheck()
{
	echo "Enter csv file name that containing ip or web address of site"
	echo "File Name:"
	read fileName


	while read -r col1 col2
	do
		check_ping $col1
	done < $fileName
}


: '
http://172.27.27.83/home/ , KS Network
http://zerodollarmovies.com/ , Zero Dollar Movies
http://180.211.219.245/ , Anabil Adda
http://download.tetrasoftbd.com/ , Tetrasoft BD
http://172.27.27.251/ , Matchnet
http://172.27.27.252/ , Classic Network
http://172.28.28.10/ , Broadband@Home
http://172.28.28.6/ , Shihab IT
http://brothersitbd.com/ , Brothers IT
http://www.bijoy.net , Bijoy.Net Software
http://103.229.80.90/ , Film-Jogot
http://45.113.238.130/ , ATS-Media-Server
http://fs.ihub.live// , I-HUB
http://freedownloadbd.com/ , Free-Download-BD
http://220.158.235.243/ , Anabil-Adda
https://genvideos.org/ , Gen-Videos
http://220.158.235.244/phpvibe/ , My-Tube
http://tube.dfnbd.net/ , DFN-BD-Tube
http://www.vdobite.com/ , VDO-BITE
http://vdomela.com/ , Video-Mela
http://broadbandathome.com/index-2.html , Broadband@Home
http://172.28.28.10/index2.html , PC-Software
http://www.ontohinbd.com/, Ontohin BD
http://www.ftpbd.net/, FTP-BD 
http://172.16.50.4/, Sam Online
http://172.16.50.2/live/, Sam Online Live  
http://15.1.1.1/, Circle Network 
http://index.ftpbd.net/, B Net 
http://www.dnetbd.com/, DNET 
http://10.1.1.1/, Bot-Tola 
http://172.27.27.83/home, KS Network
http://mojaloss.net/, Moja Loss 
https://genvideos.org/, Gen Videos 
http://103.14.27.27:8082/, Voot BD 
http://ftp.bokashoka.com/, Boka Shoka 
http://172.27.27.5/ Dhaka-Torrent
http://103.25.120.119/ PC-Software-2
http://172.27.27.253/, KS Gaming Realm
http://game.zxonlinebd.com/, Game Portal
http://pegleg.it/, Pegleg
http://www.bigfiveglories.com/, Big Five Glories
http://banglamovieo.blogspot.com/, Bangla Movies
http://www.banglafilmhd.net/, Bangla Film HD
http://www.fullbanglamovie.com/, Bangla Movies-2
http://www.dailyvision.tv/, Bangla Natok
http://www.banglanatokhd.com/, Bangla Natok HD
http://172.28.28.1/tv/, Live TV
http://www.jagobd.com/, Web TV
http://www.bdixmedia.com/, Internet TV
http://www.filehippo.com/, Filehippo Software
http://www.bijoy.net/?page_id=284, Bijoy.Net Software
ftp://172.28.28.1/, Eirtel Software
http://172.27.27.253/, KS Gaming Realm
http://game.zxonlinebd.com/, Game Portal
http://172.28.28.1/tv/, Live TV
http://www.jagobd.com/, Web TV
http://www.bdixmedia.com/, Internet TV
http://www.join4films.com/ , Join4Films
http://103.25.120.119/ , TV Shows
http://178.216.250.167/Film/ , Film
http://103.25.120.119 , 3D Movies
http://freetorrentbd.com/  , Free-Torrent-BD
http://172.27.27.249/home/, Dhaka Download
http://172.28.28.1/, Eirtel BD
http://www.torrentbd.com/ , Torrent-BD
www.naturalbd.com/ , Natural-BD
http://www.netvizmedia.net/ , All-News
http://torrent.dfnbd.net/ , Dfnbd
http://www.timepassbd.com/, Timepass BD
http://www.antbd.com/home/, Antaranga Dot Com
http://www.bdixmedia.com/, BDIX FTP
http://172.27.27.5/, Dhaka Torrent
http://www.crazyhd.com/, CrazyHD Torrent
http://172.27.27.4/besttorrent/, Best Torrent
http://www.torrentbd.com/, Torrent BD
http://www.paitara.com/, Paitara Torrent
http://server.paitara.com/, Paitara 2
http://bdixtorrenthome.blogspot.com/, BDIX Torrent
http://tube.dfnbd.net/, DFN Tube
http://172.27.27.84/, Narm Tube
http://tube.naturalbd.com/, Natural BD Tube
http://172.27.27.233/, UTURN TV Show
http://172.27.27.250/, Matchnet TV Show
http://www.filehippo.com/, Filehippo Software
ftp://172.28.28.1/, Eirtel Software
http://doridro.com/  , Doridro
http://www.ontohinbd.com/torrent/  , Ontohinbd Torrent
http://www.azibtorrent.com/  , Azibtorrent Torrent
http://www.tepantorbd.com/  , Tepantorbd Torrent
http://www.ontohinbd.com/ , Ontohinbd Torrent2
http://games.naturalbd.com:81/games/games/ , Games
http://103.25.120.119/index.php?dir=Games/ , Games-2
http://www.ihub.live/ , I-Hub-TV
http://pipexbd.com/tv/ , Pipex-TV
http://www.jagobd.com/ , Jagobd-TV
http://tv.ebox.live/ , Ebox-TV
http://www.tvsports.ml/ , TV-Sports
'