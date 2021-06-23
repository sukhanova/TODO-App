"use strict";

function showProjectDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();

	$.post('/details', inputName, (res) => {
		$('#show-title').html(`${res.name}`)
	});

	$.post('/details', inputName, (res) => {
		$('#show-description').html(`${res.description}`)
	});

	$.post('/details', inputName, (res) => {
		$('#show-start-date').html(`${res.start_date}`)
	});

}

$('#select-details').on('submit', showProjectDetails);