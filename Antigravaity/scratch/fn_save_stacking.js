function () {

	return new Promise(function (resolve, reject) {

		if (is_url_contains_string('Indexing')) {

			arraied = toArray();
			console.table(arraied);
			var jsonString = JSON.stringify(arraied);
			var OrderUID = $('#OrderUID').val();
			var CLSTokenNo = $('#CLSTokenNo').val(); /*@Desc STX-6835 - Double screen issue @Author Jain @On Sep 27 2024*/
			var NewAddedPage = AddedPages;
			  AddedPages = [];
			  var NewRemovedPages = RemovedPages;
			  RemovedPages = [];

			// var $dataobject = {
			// 	"data": jsonString,
			// 	"OrderUID": OrderUID
			// };
			// SendAsyncAjaxRequest('POST', 'Indexing/PageInsert', $dataobject, 'json', true, true, function () {
			var $dataobject = {
				"AddedPages" : NewAddedPage, "RemovedPages": NewRemovedPages,"OrderUID":OrderUID, "CLSTokenNo":CLSTokenNo /*@Desc STX-6835 - Double screen issue @Author Jain @On Sep 27 2024*/
			};
			SendAsyncAjaxRequest('POST', 'Indexing/PageInsertLatest', $dataobject, 'json', true, true, function () {
				// addcardspinner($('#AuditCard'));

			}).then(function (data) {

				resolve(data);
			}).catch(function (error) {

				console.log(error);
				reject(error);
			});
		} else {
			resolve('Success');
		}
	});
}