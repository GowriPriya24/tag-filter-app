
import sqlite3

data = [
    {
        "img": "images/Montreal1.jpg",
        "title": "Mount Royal",
        "season": "Summer",
        "day": "Monday",
        "date": "2024/08/12",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/Bonjour_montreal.jpg",
        "title": "Bonjour Montreal",
        "season": "Summer",
        "day": "Tuesday",
        "date": "2024/07/06",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/centre-ville-montreal.jpg",
        "title": "Centre Ville Montreal",
        "season": "Winter",
        "day": "Wednesday",
        "date": "2024/12/05",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/montreal2.jpg",
        "title": "Biosphere Montreal",
       "season": "Summer",
       "day": "Thursday",
       "date": "2024/08/10",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/ontario1.jpg",
        "title": "Toronto CN Tower",
        "season": "Summer",
        "day": "Friday",
        "date": "2024/08/24",
        "company": "Photos",
        "category": "ontario",
    },
    {
        "img": "images/ng1.jpg",
        "title": "Niagara Falls",
        "season": "Summer",
        "day": "Saturday",
        "date": "2024/06/10",
        "company": "Photos",
        "category": "ontario",
    },
    {
        "img": "images/ontario2.jpg",
        "title": "Toronto Fall Colors",
        "season": "Fall",
        "day": "Sunday",
        "date": "2024/09/26",
        "company": "Photos",
        "category": "ontario",
    },
    {
        "img": "images/montreal3.jpg",
        "title": "Notre-dame Basilica of Montreal",
        "season": "Fall",
        "day": "Monday",
        "date": "2024/09/23",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/montreal4.jpg",
        "title": "Olympic Stadium",
        "season": "Winter",
        "day": "Tuesday",
        "date": "2024/12/07",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/ontario3.jpg",
        "title": "Thousand Islands",
        "season": "Fall",
        "day": "Wednesday",
        "date": "2024/10/02",
        "company": "Photos",
        "category": "ontario",
    },
    {
        "img": "images/ottawa1.jpg",
        "title": "Parliament Building",
        "season": "Summer",
        "day": "Thursday",
        "date": "2024/05/07",
        "company": "Photos",
        "category": "ottawa",
    },
    {
        "img": "images/ottawa2.jpg",
        "title": "Ottawa",
        "season": "Winter",
        "day": "Friday",
        "date": "2024/01/31",
        "company": "Photos",
        "category": "ottawa",
    },
    {
        "img": "images/ottawa3.jpg",
        "title": "OTTAWA",
        "season": "Fall",
        "day": "Saturday",
        "date": "2024/09/19",
        "company": "Photos",
        "category": "ottawa",
    },
    {
        "img": "images/banff1.jpeg",
        "title": "Banff National Park",
        "season": "Fall",
        "day": "Sunday",
        "date": "2024/10/15",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/banff2.jpg",
        "title": "Lake Louise",
        "season": "Winter",
        "day": "Monday",
        "date": "2024/12/31",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/banff3.jpeg",
        "title": "Banff",
        "season": "Summer",
        "day": "Tuesday",
        "date": "2024/04/17",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/montreal5.jpg",
        "title": "Old Montreal",
        "season": "Summer",
        "day": "Wednesday",
        "date": "2024/04/27",
        "company": "Photos",
        "category": "montreal",
    },
    {
        "img": "images/banff4.jpeg",
        "title": "Welcome to Banff",
        "season": "Fall",
        "day": "Thursday",
        "date": "2024/11/03",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/banff5.jpg",
        "title": "Banff Mountains",
        "season": "Winter",
        "day": "Friday",
        "date": "2024/02/14",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/banff6.jpg",
        "title": "Banff",
        "season": "Winter",
        "day": "Saturday",
        "date": "2024/03/07",
        "company": "Photos",
        "category": "banff",
    },
    {
        "img": "images/toronto.jpg",
        "title": "Toronto",
        "season": "Fall",
        "day": "Sunday",
        "date": "2024/11/27",
        "company": "Photos",
        "category": "ontario",
    },
    {
        "img": "images/birthdayimg.jpeg",
        "title": "Birthday Song",
       
        "company": "Music",
        "playlist": "birthday",
        "audioSrc": "media/birthday.mp3"
    },
    {
        "img": "images/jaz1.jpeg",
        "title": "Jazz Music",
        
        "company": "Music",
        "playlist": "jazz",
        "audioSrc": "media/jazz.mp3"
    },
    {
        "img": "images/jaz2.jpg",
        "title": "You Got Jazz",
       
        "company": "Music",
        "playlist": "jazz",
        "audioSrc": "media/jazz2.mp3"
    },
    {
        "img": "images/dance0img.jpeg",
        "title": "Dance Zero",
       
        "company": "Music",
        "playlist": "dance",
        "audioSrc": "media/dance0.mp3"
    },
    {
        "img": "images/talent.jpg",
        "title": "Talent in the Air",
       
        "company": "Music",
        "playlist": "dance",
        "audioSrc": "media/talentdance.mp3"
    },
]

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


connection.commit()
connection.close()
