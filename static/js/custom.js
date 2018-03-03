$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function() {
      var i = $("#instance_id").val()
      new jBox('Modal', {
          attach: '#snapshots',
          width: 400,
          title: 'Create Snpshots',
          overlay: true,
          ajax: {
            url: '/create_snapshots',
            data: {
              id: i
            },
            reload: 'strict'

    }
    });

    });