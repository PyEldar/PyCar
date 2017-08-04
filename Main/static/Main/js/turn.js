  function turn(){
      var number = parseInt(document.getElementById("val").value);
      var calculatedNumber = ((number * 2.5) + 75) / 10.0; 
      if(calculatedNumber > 9){ calculatedNumber = 9;}
      if(calculatedNumber < 6){ calculatedNumber = 6;}
      //document.getElementById("Debug").value = calculatedNumber;
      $.ajax({
          url : document.getElementById("val").form.action,
          type: document.getElementById("val").form.method,
          data: {val: calculatedNumber}
      });
  };        
  
  var sendTurn = setInterval(turn, 100);
       
