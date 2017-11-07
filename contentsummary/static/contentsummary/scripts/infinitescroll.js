// init controller
  var controller = new ScrollMagic.Controller({loglevel: 1});

  // build scene
  var scene = new ScrollMagic.Scene({triggerElement: "#loader", triggerHook: "onEnter", offset:-500})
          .addTo(controller)
          .on("enter", function (e) {
            if (!$("#loader").hasClass("active")) {
              $("#loader").addClass("active");
              // simulate ajax call to add content using the function below
              setTimeout(loadNextSession, 1000);
            }
          });

  function loadNextSession () {
    $("#loader").removeClass("active");
    $.get( "/test/next", function( data ) {
      $( "#newcontent" ).append( data );
    });

    var slides = document.querySelectorAll("section.panel")

    new ScrollMagic.Scene({
      triggerElement: slides[slides.length-1],
      reverse: true,
      triggerHook: 'onLeave',
      offset: slides[slides.length-1].clientHeight*.5
    })
    .setTween(TweenMax.to(slides[slides.length-1], .75,{ opacity: 0 }))
    .addTo(controller);
    

    // "loading" done -> revert to normal state
    scene.update(); // make sure the scene gets the new start position
    
  }

