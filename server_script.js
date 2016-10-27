// The family tree and relationships can be represented as a DAG


// Tasks
// 1. Code for graph representation
//     
// 2. Code for path representation

// 3. Code for read/write from database

"use strict";
// Self invoking function at the top
(function (){
   
    var Node = {
	this.id = -1;
        this.children = [];
        this.parent = [];
        this.spouse= [];
    }

    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('RelativeDatabase');


    
    //create and remove in the graph
    this.add = function()
    {
	//TODO: Make sure the id is passed in and it is valid
	switch(arguments[0]) {
	case "node":
	    // Create a node here
	    aNode = new Node();
	    aNode.id = argument[1];
	    break;

	case "child":
	    // Check the id exists
	    child = argument[1]
	    
	    findInDatabase(argument[2])
	    break;

	case "parent":
	    
	    break;

	case "sibling":
	    
	    break;

	default:
	    break;
	}

	return 
    };

    this.remove = function(){
	switch(arguments[0])
	{
	    
	}
    };

    
    try{
        // open the database
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
