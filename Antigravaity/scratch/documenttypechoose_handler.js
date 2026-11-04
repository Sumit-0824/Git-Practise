function (e) {
      e.preventDefault();
      $('.stackdropdown').attr('data-selected-scroll-reclassify-page',''); // STX-6621

          // if( $(e.target).hasClass('documenttypechoose')) alert('got it!');
      let documenttype = $(this).closest('li').attr('data-documenttype');
      console.log(documenttype)
      let parentcategory = $(this).closest('li').attr('data-parentcategory');
      console.log(parentcategory)
      let element = $(this); 
      let documenttype_select = $('.stackdropdown').find('option');
      $.each(documenttype_select, function (key, val) { 
        if ($(val).attr('data-mastercategory') == parentcategory && $(val).attr('data-mastersubcategory') == documenttype) {
          $(val).prop('selected', true);
          $('.categoryhighlight').removeClass('categoryhighlight')
          $(element).find('a:first').trigger('click');
          $(element).closest('div').addClass('categoryhighlight');

          return;
        }
      })
    }