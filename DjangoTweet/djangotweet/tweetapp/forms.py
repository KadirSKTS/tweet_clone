from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label='nick name', max_length=10)
    massage_input = forms.CharField(label='massage', max_length=100,widget=forms.Textarea(attrs={'class':'tweetmassage'}))