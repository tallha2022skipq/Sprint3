#!/usr/bin/env python3
import os

import aws_cdk as cdk

from Sprint3.Sprint3_stack import Sprint3Stack


app = cdk.App()
Sprint3Stack(app, "TallhaIjazSprint3Stack",
    

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
