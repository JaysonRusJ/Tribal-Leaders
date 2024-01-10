// Listen to serach bar, call functions when user types into search bars 
document.getElementById("myInput").addEventListener("keyup",tableSearch);
document.getElementById("myInputLeader").addEventListener("keyup",LeaderSearch);

// Enables search feature to find a specific tribe by name
// https://www.youtube.com/watch?v=eLQhybnA9hw&t=619s reference YT video 
function tableSearch() {

   let input, filter, table, tr, td, txtValue;

   // initialize variables
   input = document.getElementById("myInput");
   filter = input.value.toUpperCase();
   table = document.getElementById("ourTable");
   tr = table.getElementsByTagName("tr");

   // for each row in the table
   for (let i = 0; i < tr.length; i++) {

      // grab the table data 
      td = tr[i].getElementsByTagName("td")[0];

      if (td) {

         txtValue = td.textContent || td.innerText;
         
         if(txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
         }

         else {
            tr[i].style.display = "none";
         }
      } // close if

   } // close for

} // close tableSearch

// Enables search feature to find a specific leader by name
// https://www.youtube.com/watch?v=eLQhybnA9hw&t=619s reference YT video 
function LeaderSearch() {
   let input, filter, table, tr, td, txtValue;

   // initialize variables
   input = document.getElementById("myInputLeader");
   filter = input.value.toUpperCase();
   table = document.getElementById("ourTable");
   tr = table.getElementsByTagName("tr");

   // for each row in the table
   for (let i = 0; i < tr.length; i++) {

      // grab the table data
      td = tr[i].getElementsByTagName("td")[1];

      if (td) {

         txtValue = td.textContent || td.innerText;

         if(txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
         }

         else {
            tr[i].style.display = "none";
         }
      } // close if

   } // close for

} // close tableSearch