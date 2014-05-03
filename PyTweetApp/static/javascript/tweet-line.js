function replyTweet(username) {
	$('#new-tweet').modal('show');
	$("#id_tweet_message").val("@" + username);
}