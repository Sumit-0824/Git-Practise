function (e) {
	var button = $(this);
	var button_text = $(this).html();
	var OrderUID = 350262;
	var CLSTokenNo = $('#CLSTokenNo').val();
	$.ajax({
		type: "POST",
		url: 'https://laravel.stacxuat.com/CommonController/UnClassify_Count',
		data: {'OrderUID' : OrderUID,"CLSTokenNo":CLSTokenNo}, 
			dataType: 'json',
		cache:false,
		success: function(res)
		{
			//Added by priya[STX-5269]
				var result = res.result;
				var data = res.datas;
				var CLSUserName = res.CLSUserName;
				var CLSUserUID = res.CLSUserUID;
				var user_uid = res.user_uid;
				var oCLSTokenNo = res.CLSTokenNo;/*@Desc STX-6835 - Double screen issue @Author Jain @On Sep 19 2024*/

				/*@Desc STX-7622 - New Ticket 10555475650-P2 - Order stuck on Auto Data Extraction due to duplicate complete classification START @Author Jain @On Nov 18 2025*/
				var clsalreadycompleted = res.clscompleted;
				if(clsalreadycompleted == 1){
					swal({
						title: "",
						text: "Classification workflow is already completed.",
						icon: "error",
						dangerMode: false,
					}).then(function () {
						// Redirecting the page to myloans
						window.location.href = base_url + "Transactions";
					});
					return false;
				}
				/*@Desc STX-7622 - New Ticket 10555475650-P2 - Order stuck on Auto Data Extraction due to duplicate complete classification END @Author Jain @On Nov 18 2025*/
		    
			if (data ==0 || data == NaN) {
				swal({
					title: 'Are you sure ?',
					text: 'Do you want to complete the Classification !',
					icon: "warning",
						showCancelButton: true,
						confirmButtonClass: 'btn btn-success',
						cancelButtonClass: 'btn btn-danger',
						buttonsStyling: false,
						closeOnClickOutside: false,
						allowOutsideClick: false,
						showLoaderOnConfirm: true,
						position: 'top-end',
						className: "swal_auto_width",
						buttons: {
							cancel: "Cancel",
							catch: {
								text: "Complete & Go to My Loans!",
								value: "catch",
								className:"btn-success",
							},
						},
					}).then(function (confirm) {

						if (confirm == "defeat" || confirm == "catch") {

							var complete_action = 0;
							if (confirm == "catch") {
								var complete_action = "Transactions";
							}

							$(button).prop('disabled', true);
							$(button).html('Completing...');
							/*Desc To show the loaded for Classification Complete @Karthiga*/
							$('.page_loader_div').show();
							var OrderUID = $('#OrderUID').val();

							fn_save_stacking().then(function () {

								// Call Stackin complete
								stacking_complete(button, button_text, complete_action);
							}).catch(function () {});
						}

					}, function (dismiss) {});
				}
				else
				{
					swal({
						title: "Sorry, we couldn't complete your request",
						text: "Please classify the unclassified pages.",
						icon: "warning",
						dangerMode: false,
					});
				}
			},
				error: function (jqXHR, textStatus, errorThrown) {
					console.log(errorThrown);
				},
				failure: function (jqXHR, textStatus, errorThrown) {
					console.log(errorThrown);
				},
		});
}