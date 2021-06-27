"use strict";

function showProjectDetails(evt) {
	evt.preventDefault();

	const inputName = $('#select-details').serialize();

	$.post('/details', (response) => {
		$('#show-details').html(`${response.name} ${response.description} ${response.description}`)
	});

}

$('#select-details').on('submit', showProjectDetails);