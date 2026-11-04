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
      PageNos.forEach(PageNo => {
        $('.sortable li .leaf[data-category="' + PageNo + '"]').remove();
      });
      resetMultiSelectedPages(); // reset selected pages
      selection = 'prepend';
    } // end here STX-6621
    
    // let FindingPageNodes = $(ol_sortable).find('[data-category="'+tpages+'"]').length;
    
    // if (FindingPageNodes == 0) {

    $.each(SubCategory, function (key, val) { 
      if ($(val).attr('data-category') == mastercategory) {
        let documenttype = $(val).find('li');  
        $.each(documenttype, function (k, elem) { 
          if ($(elem).attr('data-documenttype') == mastersubcategory) {
            var InstanceUID = $(elem).attr('id');

            if((reClassifyFlag && reclassifyPageAfter && $(elem).find('ol.nested.active li[data-category="' + reclassifyPageAfter + '"]').length > 0) || $(elem).children('div').first().hasClass('categoryhighlight') || $('#'+InstanceUID+' div:first').hasClass('categoryhighlight')){ // Condition "(reClassifyFlag && reclassifyPageAfter && $(elem).find('ol.nested.active li[data-category="' + reclassifyPageAfter + '"]').length > 0)" Added by Sathishkumar R on 29 June 2024. STX-6621
              PageNos.forEach(PageNo => {
                if ($(elem).attr('data-instance')) {
                  if ($(elem).find('ol').length == 0) {
                    $(elem).append('<ol class="nested active"></ol>');
                    $(elem).find('ol.nested.active').append('<li id="list_30" class="leaf" data-root="'+$(elem).attr('data-documenttype')+'" data-branch="'+$(elem).attr('data-documenttype')+'" data-category="'+PageNo+'" data-type="page"><div><a class="classified_page" href="#page='+PageNo+'"> Page '+PageNo+'<i class="fas fa-times DeleteElement" title="Remove classification" style="margin-left: 17px;fill: transparent;"></i></a> <i class="icon-cross3 DeleteElement" title="Remove classification"></i></li>');/*@Desc Classification optimization - Save required Pages @Author Jain @On Mar 14 2024*/
                  }
                  else{

                    // Multiple Page re-classification using scroll. Added by Sathishkumar R on 29 June 2024. STX-6621
                    var selectedElement = $(elem).find('ol.nested.active');
                    if (reClassifyFlag && reclassifyPageAfter !== undefined && reclassifyPageAfter !== '') {
                      selection = 'after';
                      selectedElement = $(elem).find('ol.nested.active li[data-category="' + reclassifyPageAfter + '"]');
                    }
                    // end here STX-6621

                    selectedElement[selection]('<li id="list_30" data-root="'+$(elem).attr('data-documenttype')+'" data-branch="'+$(elem).attr('data-documenttype')+'" class="leaf" data-category="'+PageNo+'" data-type="page"><div><a class="classified_page" href="#page='+PageNo+'"> Page '+PageNo+'<i class="fas fa-times DeleteElement" title="Remove classification" style="margin-left: 17px;fill: transparent;"></i></a> <i class="icon-cross3 DeleteElement" title="Remove classification"></i></li>');/*@Desc Classification optimization - Save required Pages @Author Jain @On Mar 14 2024*/ /*"selectedElement[selection]" Added by Sathishkumar R on 29 June 2024. STX-6621*/
                  }
                }else{
                  var elements='';elements1='';
                  var id = $(this).attr('data-position');

                  var elementLength = $(".mainDocLI-"+id+" .DocumentTypeName").length;

                  var arr = [];
                  $( ".mainDocLI-"+id+"  .DocumentTypeName" ).each(function( index ) {
                    if ($( this ).attr('data-instance') !== undefined) {
                      arr.push(parseInt($( this ).attr('data-instance')));
                    }
                  });
                  arr.sort();

                  var MissingValues=getMissingNumber(arr);

                  if (MissingValues!='-1') {
                    elementLength = MissingValues;
                  }
                  elements =elements+'<li id="'+InstanceUID+'_'+elementLength+'" class="leaf-branch DocumentTypeName" data-documenttype="'+$(elem).attr('data-documenttype')+'" data-category="'+$(elem).attr('data-documenttype')+'" data-parentcategory="'+$(elem).attr('data-documenttype')+'" data-type="subcategory" data-instance="'+elementLength+'"><div class="collapse-li-subcategory"><span class="right-caret"></span><a href="javascript:void(0);" class="documenttypechoose menu_doctype_list_child" > '+$(elem).attr('data-documenttypename')+' - '+elementLength+'<i class="fas fa-times DeleteDocElement" title="Remove a document" style="margin-left: 17px;fill: transparent;" data-id="'+InstanceUID+'_'+elementLength+'"></i></a></div>';/*@Desc STX-7498 - Classification screen UI changes @Author Jain @On Aug 22 2025*/


                  elements1=elements1+'<ol class="nested active"><li id="list_30" data-root="'+$(elem).attr('data-documenttype')+'" data-branch="'+$(elem).attr('data-documenttype')+'" class="leaf" data-category="'+PageNo+'" data-type="page"><div><a class="classified_page" href="#page='+PageNo+'" style="color:#069067 !important;"> Page '+PageNo+'<i class="fas fa-times DeleteElement" title="Remove classification" style="margin-left: 17px;fill: transparent;"></i></a> <i class="icon-cross3 DeleteElement" title="Remove classification"></i></li></ol>';

                  $(elem).after(elements);
                  $("#"+InstanceUID+"_"+elementLength).append(elements1);
                  elem = $('#'+InstanceUID+'_'+elementLength+''); // For single and new instance creation Edited By Harshita on 05 July 2024 STX-6621 STX-6702
                }
                  /*@Desc push page to sort list @Author Jainulabdeen @Added on Dec 4 2020*/
                const DocumentTypeName = DocumentTypes.find(DocTypes => DocTypes.CategoryHash == $(elem).attr('data-documenttype'));
                if($(elem).attr('data-instance') !== undefined){
                  var Instance = $(elem).attr('data-instance');
                } else {
                  var Instance = elementLength;
                }
                console.log(Instance);
                  /*@Desc Ascending order rather than docs going to the bottom of the page when recls happens - START @Author Jain @On Aug 16 2023*/
                if(StackPagesASC == '1'){ // "!reClassifyFlag" Condition Added by Sathishkumar R on 29 June 2024. STX-6621 /*STX-7205 removed the condition for reclassified higlight*/
                  if ($(elem).attr('data-instance')) {
                    var divas = elem;
                  }else{
                    var divas = "#"+InstanceUID+"_"+Instance;
                  }
                  divArr = $(divas).find('ol.nested.active li.leaf');
                    /*divArr.sort(function(a, b) {
                      return $(a).find("a.classified_page").text().trim() > $(b).find("a.classified_page").text().trim() ? 1: -1;
                    });*/
                    var removeDocumentTypeA = [];/*array for page remove document edited by Harshita on 14 March 2025 STX-7205*/
                  divArr.sort((a,b) => $(a).find("a.classified_page").text().trim().split("Page").pop().trim() - $(b).find("a.classified_page").text().trim().split("Page").pop().trim());
                  $(divas).find('ol.nested.active').html(divArr);
                  /*@Desc Classification optimization - Save required Pages - START @Author Jain @On Mar 14 2024*/
                    $(divas).find('ol.nested.active li.leaf').each(function (key, value) {
                      var PageNo = $(value).attr('data-category');
                      RemovedPages = RemovedPages.filter(function(el) { return el.PageNo != PageNo; });
                      AddedPages = AddedPages.filter(function(el) { return el.PageNo != PageNo; });
                      AddedPages.push({'PageNo' : PageNo , 'DocumentTypeName' : DocumentTypeName.DocumentTypeName, 'documenttype' : $(elem).attr('data-documenttype') , 'Instance' : Instance, 'PagePosition' : key+1});
                      /*for updated page number array Added By Harshita on 13 March 2025  STX-7205*/
                      $(value).attr('data-position',key+1);/*STX-7205*/
                      let exists = PageNoForHighlightCompareArray.filter(pageCompare => pageCompare.pageNo == PageNo);
                      if (exists.length > 0) {
                        if((exists[0].instance != Instance) || (exists[0].documentType != $(elem).attr('data-documenttype')) || (exists[0].position != (key+1)) ){
                          PageNoForHighlight.push(PageNo);
                          if((exists[0].instance != Instance) || (exists[0].documentType != documenttype)){
                            let existsR = removeDocumentTypeA.some(removeDocumentTypeV => (removeDocumentTypeV.removeDocumentType == exists[0].documentType && removeDocumentTypeV.instance == exists[0].instance));
                            if(!existsR){
                              removeDocumentTypeA = [...removeDocumentTypeA,{'documentType':exists[0].documentType,'instance':exists[0].instance}];
                            }
                          }
                        }else{
                          PagePositionArray.push(PageNo);
                        }
                      }/* end here STX-7205*/
                    });
                    /*for reclassify page highlight Added by Harshita on 14 March 2025 STX-7205*/
                    if(removeDocumentTypeA.length > 0){
                      removeDocumentTypeA.forEach(function(removeDocumentTypeV) {
                        storeRemovePageDocumentType(removeDocumentTypeV.documentType,removeDocumentTypeV.instance);
                      });
                    }/* end here STX-7205*/
                  }else{
                    RemovedPages = RemovedPages.filter(function(el) { return el.PageNo != PageNo; });
                    AddedPages = AddedPages.filter(function(el) { return el.PageNo != PageNo; });
                    AddedPages.push({'PageNo' : PageNo , 'DocumentTypeName' : DocumentTypeName.DocumentTypeName, 'documenttype' : $(elem).attr('data-documenttype') , 'Instance' : Instance}); /*@Desc Classification optimization - Save required Pages - END @Author Jain @On Mar 14 2024*/
                    /*@Desc Classification optimization - Save required Pages - END @Author Jain @On Mar 14 2024*/
                    /*for updated page number array Added By Harshita on 13 March 2025  STX-7205*/
                      let exists = PageNoForHighlightCompareArray.filter(pageCompare => pageCompare.pageNo == PageNo);
                      if (exists.length > 0) {
                        if((exists[0].instance != Instance) || (exists[0].documentType != $(elem).attr('data-documenttype')) ){ /*|| (exists[0].position != (key+1)) */
                          PageNoForHighlight.push(PageNo);
                        }else{
                          PagePositionArray.push(PageNo);
                        }
                      }/* end here STX-7205*/
                }
                console.log('AddedPages',AddedPages);
                console.log('RemovedPages',RemovedPages);
                  /*@Desc Ascending order rather than docs going to the bottom of the page when recls happens - END @Author Jain @On Aug 16 2023*/
                NewSortPage.push({'PageNo' : PageNo , 'DocumentTypeName' : DocumentTypeName.DocumentTypeName, 'documenttype' : $(elem).attr('data-documenttype') , 'Instance' : Instance});
                  /*end*/

                RemovedPages.push({'PageNo' : PageNo}); // Add reclassified pages into RemovedPages array. Added by Sathishkumar R on 29 June 2024. STX-6621
              });

    console.log('Active', $(elem).find('.nested'));
    if ($(elem).find('.nested').not('.active')) {
      $(elem).find('.nested').addClass('active');
    }
    console.log('Caret', $(elem).find('.right-caret'));
    if ($(elem).find('.right-caret').not('.right-caret-down')) {
      $(elem).find('.right-caret').addClass('right-caret-down');
    }

    unsort();

  }
}
})
  }
})
    // }
    
    if (reClassifyFlag) { // STX-6621
      resetReclassifyDestination();
    } // end here STX-6621
    
  }