from django import forms



class SendMail(forms.Form):
	subject = forms.CharField(label="Subject",
                              max_length=1000,
                              widget=forms.TextInput(
                                                     attrs={"placeholder": "Write the subject",
                                                            'size':31}
                                                    )
                             )

	message = forms.CharField(label="Message",
                              max_length=1000,
                              widget=forms.TextInput(
                                                     attrs={"placeholder": "Write your message",
                                                            "size":31}
                                                    )
                             )



