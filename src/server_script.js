// The family tree and relationships can be represented as a DAG





// Tasks
// 1. Code for read/write from database
//
// 2. Code for graph representation
//     
// 3. Code for path representation

"use strict";
// Self invoking function at the top
(function (){
   
    var Node = {
	this.id = -1;
        this.children = [];
        this.parent = [];
        this.spouse= [];
    }

    
    //Database manipulation
    this. = function(relativeIdentifier){
	'SELECT id FROM RelativeDetails WHERE first_name = \'' '\' OR last_name = \'Gigoo\''),

	
    }

    this.databaseManipulation = function(cmdStr){

    	if (cmdStr.split(" ",1) === "get"){
    	    this.db.get(cmdStr);
    	}

	
    }


    
    try{
        // open the database
	var sqlite3 = require('sqlite3').verbose();
	this.db = new sqlite3.Database('RelativeDatabase');



	db.serialize(
	    function(){

		function RelativeInfo() {		    
		    RelativeInfo.genderOptions = ["male","female","unknown"];
		    this.first_name = '';
		    this.middle_name = '';
		    this.last_name = ''
		    this.address =''
		    this.nickname =''
		    this.gender = 0;
		};

		// 1. Inserting new record
		var relative = new RelativeInfo();
		relative.first_name = 


		sqlStatement = 'INSERT INTO RelativeDetails (first_name, middle_name, last_name, address, nickname, gender) VALUES
(\''+relative.first_name+'\', \'' +relative.middle_name+'\', 
\''+relative.last_name+ '\', \''+relative.address+'\', \''+relative.nickname+ '\', '+relative.gender+ ');';

		db.run(sqlStatement);

		
		//2. Getting new record

	    }

	);


        // Depending upon operation selected - findPath or manipulate Database
	argument_list = arguments;
	option = arguments_list.splice(0,1);
	
	//Reflection needed
	switch(option){
	case "add" : 
	    {
		add(argument_list);
		break;
	    }
	case "remove":
	    {
		remove(argument_list);
		break;
	    }
	case "view":
	    {
		view(argument_list);
		break;
	    }
	default:
	    console.error(new Error("The 1st argument couldn't be identified"));
	}




        //commit the transactions and changes into the Database
    }catch(err){

    } finally{   
        //close the database
    }
})();
