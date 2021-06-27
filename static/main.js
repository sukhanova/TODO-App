// "use strict";



// $("#select-details").on("submit", (evt) => {
// 	evt.preventDefault();

// 	const formInputs = {
// 		name: $('#project-title').val()
// 	};
// 	$.ajax({
// 		url:'/details',
// 		data: JSON.stringify(formInputs),
// 		contentType: "application/json",
// 		success: (response)=>{
// 			$('#show-title').html(`${response.name}`)
// 		},
// 		method: "POST",
// 	});
// });



function showProjectDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();

	$.post('/details', inputName, (response) => {
		$('#show-title').html(`${response.name}`)
	});

	$.post('/details', inputName, (response) => {
		$('#show-description').html(`${response.description}`)
	});

	$.post('/details', inputName, (response) => {
		$('#show-start-date').html(`${response.start_date}`)
	});

}

$('#select-details').on('submit', showProjectDetails);