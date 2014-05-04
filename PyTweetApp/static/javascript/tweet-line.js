function replyTweet(username) {
	$('#new-tweet').modal('show'); // showing modal to enter a new tweet
	$("#id_tweet_message").val("@" + username + " "); // adding to the form the name the user want to mention 
}