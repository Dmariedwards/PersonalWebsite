$('document').ready(function() {

     // We need to duplicate the whole body of the website so if you scroll down you can see both the bottom and the top at the same time. Before we do this we need to know the original height of the website.
     var origDocHeight = document.body.offsetHeight;

     // now we know the height we can duplicate the body    
     $("#main").contents().clone().appendTo("body");


     $(document).scroll(function(){ // detect scrolling

         var scrollWindowPos = $(document).scrollTop(); // store how far we have scrolled

         if(scrollWindowPos >= origDocHeight ) { // if we scrolled further then the original doc height
             $(document).scrollTop(0); // then scroll to the top
         }       
     });

 }); 
// $(document).ready(function(){
//     $("#hide").click(function(){
//         $("embed").hide();
//     });
//     $("#show").click(function(){
//         $("embed").show();
//     });
// });