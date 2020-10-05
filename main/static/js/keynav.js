try {
    var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
  }
  catch(e) {
    console.error(e);
    $('.no-browser-support').show();
    $('.app').hide();
  }
  
  $(function() {
   
    
    tips=["Put on an extra layer of clothing instead of turning on the heating. Seriously doubling up on your socks does wonders!","Open up your blinds and use as much natural light as possible before switching on your light bulbs.",
    "Turn off your lights when you leave a room.",
    "Put up a no junk mail sign on your letterbox to limit the amount of paper waste.","Hang your wet clothes on a drying line or rack instead of using a powered dryer","Hand wash your clothes particularly if you only have a few items to clean.",
    "Start timing your showers. Or invest in a shower timer","Grow your own herbs, fruit and vegetables even if it’s just a few pots around the house, it all helps!",
    "Turn off your devices at night including your wifi box.",
    "Get a water-saving showerhead.","Use organic fertilisers.",
    "Purchase recycled toilet paper with plastic-free packaging.",
    "On the topic of toilets use scrap paper or newspaper or toilet paper to collect pet poo."]

    posters=["https://science.nasa.gov/files/science-pink/s3fs-public/styles/large/public/thumbnails/image/EarthDay2020_Instagram_0.jpg?itok=bvFdSz3y",
    "https://science.nasa.gov/files/science-pink/s3fs-public/styles/large/public/thumbnails/image/Earth_Day_PPT_1080x1080[1].jpg?itok=mC_7XDBF",
    "https://science.nasa.gov/files/science-pink/s3fs-public/styles/large/public/thumbnails/image/2018_EarthDay_SocialMedia.jpg?itok=UzWSqWxk"]
    document.getElementsByClassName("tip").innerHTML+=tips[Math.floor(Math.random() * tips.length)];
    document.getElementById("tip").innerHTML+=tips[Math.floor(Math.random() * tips.length)];
    $("#poster").attr('href',posters[Math.floor(Math.random() * posters.length)])

    
    $(document).keydown(function(e) {
        switch (e.which) {

               
                
                case 107:
                    $("#play").trigger("click");                        // +
                    break;
                
                case 18:
                  document.getElementById("my_audio").play();      //alt
                  break;

                case 109:
                    $(location).attr('href', $('#articles').attr('href'))         //-
                    break;
                
                case 192:
                  $(location).attr('href', $('#blogs').attr('href'))        // tilde
                  break;


                case 46:                                                    //delete
                  $(location).attr('href', $('blogWrite').attr('href'))
                                              
            
        }
  
        
    });
  });