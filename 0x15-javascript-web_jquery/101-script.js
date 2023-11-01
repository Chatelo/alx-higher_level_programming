document.addEventListener('DOMContentLoaded', function () {
  const ul = $('ul.my_list');

  // Add item
  $('#add_item').click(function () {
    ul.append('<li>Item</li>');
  });

  // Remove item
  $('#remove_item').click(function () {
    ul.children().last().remove();
  });

  // Clear list
  $('#clear_list').click(function () {
    ul.empty();
  });
});
