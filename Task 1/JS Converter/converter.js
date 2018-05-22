function calculate() {
  var entervalue = parseFloat(document.getElementById("entervalue").value);
  var input = document.getElementById("input");
  var output = document.getElementById("output");
  var outputresult = document.getElementById("outputresult");

	var rates = {
		USD : {
			USD: 1,
			GBP: 0.7,
			AUD: 1.3,	
			EUR: 0.8,
			CAD: 1.3,
		},
		GBP : {
			USD: 1.4,
			GBP: 1,
			AUD: 1.55,
			EUR: 1.14,
			CAD: 1.8
		},
		AUD : {
			USD: 0.76,
			GBP: 0.54,
			AUD: 1,
			EUR: 0.62,
			CAD: 1,
		},
		EUR : {
			USD: 1.23,
			GBP: 0.88,
			AUD: 1.6,
			EUR: 1,
			CAD: 1.6,
		},
		CAD : {
			USD: 0.77,
			GBP: 0.55,
			AUD: 1,
			EUR: 0.63
			CAD: 1,
		},
	};
	if(rates[input.value] && rates[input.value][output.value]){
		outputresult.value = entervalue * rates[input.value][output.value];
	}
	else outputresult.value = "ERROR";
}
}
