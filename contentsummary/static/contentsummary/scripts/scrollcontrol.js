console.clear();
console.log("ScrollMagic v%s loaded", ScrollMagic.version);


//add pannel# to each  panel
$(".panel").each(function(i) {
  $(this).addClass("panel" + (i + 1));
});

// how many panels
var numPanels = $('.panel').length;

// Add z-index and calulate tween durations
var orderedPanels = [];
var duration = [];
for (var i = 0; i < numPanels; i++) {
	// generate CSS for z-index of each panel, negative numbers decending
  orderedPanels.push(".panel" + (i + 1) + " {z-index: -" + (i + 1) + ";} ");
  // Calulate tween duration for each panel based on height
  console.log(($(".panel" + (i+1)).height()))
  duration.push(($(".panel" + (i+1)).height()/200));
}
// Add CSS for z-index of each panel to the head
$("<style id='panelZOrder' type='text/css'>" + (orderedPanels.join("")) + "</style>").appendTo("head");


// init
var controller = new ScrollMagic.Controller();

// define movement of panels
var wipeAnimation = new TimelineLite()
  .fromTo("section.panel.panel1", duration[0], {
    y: "0"
  },
    {
    y: "-100%",
    ease: Linear.easeNone
  })
  .fromTo("section.panel.panel2", duration[1], {
    y: "0"
  }, {
    y: "-100%",
    ease: Linear.easeNone
  });


// create scene to pin and link animation
new ScrollMagic.Scene({
    triggerElement: "#pinContainer",
    triggerHook: "onLeave",
    duration: "400%"
  })
  .setPin("#pinContainer")
  .setTween(wipeAnimation)
  .addIndicators() // add indicators (requires plugin)
  .addTo(controller);