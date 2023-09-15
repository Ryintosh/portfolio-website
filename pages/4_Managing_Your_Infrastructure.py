import streamlit as st


st.subheader("Managing")
st.write("""
         Managing your infrastructure takes a lot of work, but you know what else does? An incident.
         """)

incident,change =  st.tabs(["Incident Management", "Change Management"])

with incident:
    st.write("""Incident Management is relatively a simple concept, when your services are degrading or down try to bring it back to normal.
                Identifying an incident is the first step of this process, this can be commonly be found by having alerts, customer calls, or
                functionality the team uses is not working or is degrading. Now these indicators don't always mean it's an actual impact to anyone,
                it must be verified to become a formal incident. Once confirming the indicator to an incident is causing degradation or failure in a service,
                then calling an incident to all impacted teams to resolve the incident is the next priority. Releasing information to stakeholders and impacted
                teams in this process is a must as they can't continue business as usual actitvies without knowing the progress on the incident. Once the incident is resolved
                inform impacted teams and stakeholders of it, but resolution also includes verifying. Once this is accomplished, the job is not done yet. We need
                to do a Root Cause Analysis (RCA) on the incident. What caused this incident to occur? What steps can we take to improve the Mean Time To Resolution (MTTR)?
                What did we do during this process to resolve the incident? There are many more questions you can ask, however these prove the point that an incident
                can prove to be a great learning experience on what to watch out for and how to deal with your infrastructure better so customers aren't imapcted.
             
             
             
             """)

with change:
    st.write("""Change Management is one of the most critical processes in a company. Change is a necessary evil, however, it doesn’t have to be damaging. 
             A stable environment can easily be disrupted by changes as the results may not be known from implementing it. 
             However, the art of change management isn’t to eliminate the potential of issues but to decrease the chance of it occurring. 
             So how can we do that? First, we would want to have a formal process for implementing changes, which starts with a change request. 
             A change request should contain information:

             - What systems will be impacted
             - Teams impacted by change
             - Business justification
             - Urgency
             - Steps needed to implement this change
             - Steps to rollback the implementation of this change
             - Steps to verify the implementation was successful
             - If there is downtime
             - How long and when will the change will take place
             - Has it been tested in a lower environment
             
             Typically before a formal change request to production, there is testing done either in non-production, staging, or quality assessment (QA). 
             The reason why environments may vary is due to the financial implications of having each environment running with production. However, you could save more by spending more. 
             Why is this? It’s because changes can cause incidents, which impact customers! After having the change request finished, review with your team the steps and implications of the change. 
             Is it necessary to even implement this? Are these steps going to give us what we want? 
             Now, you have a change request completed, what do you do next with it? 
             Bring it to either the manager of your team to approve or a change advisory board (In my opinion this is almost always the better alternative). 
             The change advisory board or manager will look at your steps and objectives and approve if all the information is there. 
             Now comes the implementation of the change, which impacted teams should be contacted about it occurring and invited to the call if they wish to join. 
             If any of the steps fail, you roll back. If anyone pressures you to do an ad-hoc step, this is bad, because this is not an approved step by the change advisory board or manager. 
             This ad-hoc step was also not tested, so this only brings more chance of problems arising. Now, this could be a very important step from a business perspective, however, tell them “What is the worst that could happen if we make ad-hoc changes?”. 
             Typically it would involve breaking service level agreements with customers or internal services degrading or going down. 
             All you can do when a step fails is roll back because any remedy will have its own potential problems. 
             Alright, if your change is now completed and verified, what do you do now? A document that it had gone through successfully and inform impacted teams that it is completed.

""")
