
    function choosepage (elem) { 
      console.time("measure choosepage time"); 
      var li_checkbox = $(elem).find('.checkbox_unsorted');
  //edited by Harshita Tripathi on 09 Feb 2023 STX-3854
      if ($(li_checkbox).checked == false) {
        $(li_checkbox).prop('checked', true);
      }
      else if ($(li_checkbox).checked == true){
        $(li_checkbox).prop('checked', false);
      }
  //commented by Harshita Not Required 
  // if ($(li_checkbox).prop('checked') == false) {
  //   $(li_checkbox).prop('checked', true);
  // }
  // else if ($(li_checkbox).prop('checked') == true){
  //   $(li_checkbox).prop('checked', false);
  // }

      console.timeEnd("measure choosepage time");
    }
    function unsort()
    {
      console.time("measure unsort time");
    // var PageNo = $('#diff').val();
      let PageNos = $('.checkbox_unsorted:checked').map(function (index, element) {  
        return $(element).val();
      }).get();

      PageNos.forEach(PageNo => {
        $('ol.unsortable').find('[data-category="'+PageNo+'"]').closest('li').remove();
      });

    SortUnSort(); /*@Desc refresh suggestions @Author Jainulabdeen @Added on Dec 4 2020*/

    // var FindingPageNodes = $('ol.unsortable').find('[data-category="'+PageNo+'"]').closest('li').remove();
      console.timeEnd("measure unsort time");
    }

  /*@Desc suggestion button click to add as sort and refresh suggestions @Author Jainulabdeen @Added on Dec 4 2020*/
  //Edited By Parthasarathy on 19 Sep 2023 STX-5300
  $(document).off('click', '.documenttypechoose_sug').on('click', '.documenttypechoose_sug', async function (e) { //STX-5300
    e.preventDefault();

    /*@Desc STX-6835 - Double screen issue - START @Author Jain @On Sep 27 2024*/
    EditableCLSHashcode = localStorage.getItem("EditableCLSHashcode");
    UniqueCLSOrderUID = localStorage.getItem("UniqueCLSOrderUID");
    if(CurrentCLSTokenNo != EditableCLSHashcode || UniqueCLSOrderUID != CurrentCLSOrderUID){

      if(TokenUpdate == 1 && popup_message == ''){
      swal({
        title: '',
        text: "You are in Read-Only Mode and cannot make changes. Edit this session?",
        icon: "warning",
        buttons: {
          cancel: {
            text: "No",
            value: false,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          catch: {
            text: "Yes",
            value: "reload",
            className: "btn btn-primary",
          },
        },

        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        buttonsStyling: false,
        closeOnClickOutside: false,
        allowOutsideClick: false,
        position: 'top-end'
      }).then(function (confirm) {
        if (confirm == 'reload') 
        {
          location.reload();
        }
      });
      }else if(TokenUpdate == 1 && popup_message != ''){
        swal({
          title: "Warning",
          text: "You are in Read-Only Mode and cannot make changes. Request edit access to modify this order.",
          icon: "warning",
          button: "OK"
        });
      }
      return false;
    }
    /*@Desc STX-6835 - Double screen issue - END @Author Jain @On Sep 27 2024*/

    var Page = $(this).attr('data-page');
    var PageInstance = $(this).attr('data-instance');
    let documenttype = $(this).attr('data-documenttype');
    console.log(documenttype)
    let parentcategory = $(this).attr('data-parentcategory');
    console.log(parentcategory)
    let element = $(this); 

    //Edited By Parthasarathy on 19 Sep 2023 STX-5300
    var not_clicked = false;
    if (click_count == 0) {
      not_clicked = true;
      var response_1 = await toggleDocType();
      console.log(response_1);

    } // STX-5300
    
    $('.checkbox_unsorted').prop('checked', false);
    $('.checkbox_unsorted[value='+Page+']').prop('checked', true);
    let documenttype_select = $('.stackdropdown').find('option');
    $.each(documenttype_select, function (key, val) { 
      if ($(val).attr('data-mastercategory') == parentcategory && $(val).attr('data-mastersubcategory') == documenttype) {
        $(val).prop('selected', true);
        $('.categoryhighlight').removeClass('categoryhighlight');

        /*@Desc STX-7498 - Classification screen UI changes - START @Author Jain @On Aug 22 2025*/
        var instanceSelector = $('.documenttypechoose').closest('li[data-documenttype="' + documenttype + '"]').filter('[data-instance="1"]'); // select only instance 1

        var hasPages = instanceSelector.find('ol.nested li[data-type="page"]').length > 0;

        if (hasPages) {
          console.log('Instance 1 has pages');
        } else {
          console.log('Instance 1 has NO pages');
          PageInstance = 1;
        }
        /*@Desc STX-7498 - Classification screen UI changes - END @Author Jain @On Aug 22 2025*/

        if(PageInstance != undefined){
          $('.documenttypechoose').closest('li[data-documenttype="'+documenttype+'"]').closest('[data-instance="'+PageInstance+'"]').find('a:first').trigger('click');
          $('.documenttypechoose').closest('li[data-documenttype="'+documenttype+'"]').closest('[data-instance="'+PageInstance+'"]').find('div:first').addClass('categoryhighlight');
        } else {
         $('.documenttypechoose').closest('li[data-documenttype="'+documenttype+'"]').closest('ol').find('li:first').find('a:first').trigger('click');
         $('.documenttypechoose').closest('li[data-documenttype="'+documenttype+'"]').closest('ol').find('li:first').find('div').addClass('categoryhighlight');
       }
      // $(".popover").remove(); 
       return;
     }
   })
    sortpages();
    // SortUnSort(); /*@Desc Already calling in sortpages->unsort function so no need @Author Jain @On Mar 18 2024*/
    //Edited By Parthasarathy on 19 Sep 2023 STX-5300
    if (not_clicked == true) {
      if (documenttype) {
        var myElem = document.querySelector('li[data-documenttype="'+documenttype+'"]');
        if (myElem) {
          var topPos = myElem.offsetTop;
          document.querySelector("aside").scrollTop = topPos-(document.querySelector("aside").offsetHeight/2);        
        }

      }
    } // STX-5300
  });

  // $(document).on('drop', 'ol.sortable li li', function (e) { 
  //   // alert(); 
  //   sortpages();
  // })

  // $(document).bind('dragover', 'ol.sortable li li', function (e) {  
  //   e.preventDefault();
  //   console.log('Drag Start');
  // })

  // $(document).bind('dragstart', 'ol.unsortable li a', function (e) {  
  //   // e.preventDefault();
  //   console.log('dragstart');
  //   e.originalEvent.dataTransfer.setData("text", e.target.id);
    
  // })

  function sortpages()
  {
    // Multiple Page re-classification. Added by Sathishkumar R on 29 June 2024. STX-6621
    let PageNos;
    let reClassifyFlag = false;
    var selection = 'append';
    var reclassifyPageAfter = $('select.stackdropdown').attr('data-selected-scroll-reclassify-page');
    if (copySelectedItems.length > 0) {
      reClassifyFlag = true;
      PageNos = copySelectedItems.map(function(el){
        return $(el).attr('data-category');
      });

      // Check if any PageNos match the reclassifyPageAfter
      if (PageNos.includes(reclassifyPageAfter)) {
        swal({
          title: "Warning",
          text: "Selected page is the same as the destination page!",
          icon: "warning",
          button: "OK"
        });
        resetReclassifyDestination(); // Reset reclassify page selected destination
        return;
      }

    } else { // end here STX-6621
      // var PageNo = $('#diff').val();
      // alert("jfjf")
        PageNos = $('.checkbox_unsorted:checked').map(function (index, element) {  
        return $(element).val();
      }).get();
    }
    console.log('PageNos : ',PageNos);

    if (PageNos.length === 0) {
      swal({
        title: "Warning",
        text: "No pages selected!",
        icon: "warning",
        button: "OK"
      });
      resetReclassifyDestination(); // Reset reclassify page selected destination
      return;
    }
    
    let selected_stackdropdown = $('select.stackdropdown').find(':selected');
    // Empty destination submit validation Added by Sathishkumar R on 29 June 2024. STX-6621
    if (selected_stackdropdown.length === 0) {
      swal({
        title: "Warning",
        text: "No destination selected!",
        icon: "warning",
        button: "OK"
      });
      resetReclassifyDestination(); // Reset reclassify page selected destination
      return;
    } // end here STX-6621
    let ol_sortable = $('ol.sortable');
    
    var mastercategory = $(selected_stackdropdown).data('mastercategory');
    var mastersubcategory = $(selected_stackdropdown).data('mastersubcategory');
    // var tpages = $('#diff').val();
    
    let SubCategory = $('li.SubCategory');

    if (reClassifyFlag) { // STX-6621