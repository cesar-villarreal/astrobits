from django import forms



class SendMail(forms.Form):
	contact_mail = forms.CharField(label="Your E-Mail",
                                   max_length=30,
                                   widget=forms.TextInput(
                                                          attrs={"placeholder": "Write your E-Mail",
                                                                 "size":31}
                                                         )
                                   )

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



