"use strict";


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