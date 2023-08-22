import streamlit as st


st.subheader("Monitoring")
st.write("""
         Monitoring your infrastucture should be the process of understanding your infrastructure. If you do not understand it, how can you observe it and all of it's functions. Those that have experience
         in dealing with incidents, changes, and understanding customer needs will be most optimial in creating monitoring that is effective. If you have a team dedicated to monitoring, but is not involved with
         the previous experiences, then you may end up with a bunch of monitoring that isn't relevant to the needs of the customer using the service or not the right information for investigators to resolve incidents.
         """)

alerts,dashboards,auditing,versionControl = st.tabs(["Alerts", "Dashboards", "Auditing", "Version Control"])


with alerts:
    st.write("""
            Alerts must have a reason to exist, and that reason must be related to either cost, degradation of the
            customer experience, or predicting impacts on the former two reasons. We must craft alerts corresponding to these
            tenants as otherwise we create a large amount of alert noise. Alerting on symptomns instead of causes is a great way to start
            on alerting. Instead of alerting on cpu utilization and memory usage, we can alert on what impacts the customer such as latency or avaliability.
             This switch in alerting on causes to symptomns make it that we respond to only when the system is actually impacting the customer, because otherwise
             responders would be reacting to an alert that has no impact to anyone. Now alerting on causes is fine, if it is predictive. This can only occur
             with a deep understanding of the system, a high consistency between cause and symptomn, and if your enviornment/system is relatively stable. Let's say the
             application or size of virtual machines is changing constantly (as cloud providers make these things incredibly easy), then the chance of the causes leading to symptomns would
             have to be reunderstood.

             Alerts should contain a runbook contianing the steps tested in non-prod, teams impacted, and tools required to complete steps. When getting an alert, make it as easy as possible
             for the person recieving to contact the right people as fast as possible to reduce the Mean Time To Resolve (MTTR). Since the incident responder may not always be the
             Subject Matter Expert (SME), this is critical to maintain in alerts/runbooks. 

             With the new hype in Artifical Intelligence (AI), we see many monitoring platforms promising predictive alerting. This is a great new technology that can vastly decrease
             our MTTR, however it can also increase it. Without giving quality and quanitity of data for the AI to create a model, then we are left with predictive alerting that is
             not informed enough and misinformed. AI can only be as good as the data provided to it. All predicitive alerting should be tested in a lower environment otherwise we risk
             having just alert noise.

             Alert noise was mentioned quite often, be sure to have alerts that are timely and actionable. Some examples are that an alert fires as symptomns are showing and there can be actions done
             to remedy the alert. Otherwise you can have an alert delayed after a hour and no actions can be done to resolve it, leaving the incident responder just ignoring it as there are 
             no next steps.

             Overall, alerting needs to be done on impacts and provide steps to resolving them. Otherwise the individuals receiving the alerts could receive too many alerts and begin to ignore them. This could impact
             the customer at some point as an actual incident may come from an alert, but it will be ignored as countless others were before it.
             
             
             """)
    
with dashboards:
    st.write("""
                Dashboards are utilized to help aggregate data, real-time monitoring, and potentially predict incidents.
                When an incident occurs, you should look at the dashboard to solve your problem, and if needed look
                further into metrics/logs by identifying problem areas found in the dashboard. However, if your team
                avoids the dashboards and works straight into the metric/logs, then your dashboard is displaying
                irrelevant data. What data should we portray in the dashboard then to make incident management and
                monitoring of our systems more efficient? We should look at potential causes to an incident and what
                we alert on. Some examples can be latency. The potential causes of latency can be found potentially in
                the logs, CPU utilization, disk I/O, memory usage, network traffic, etc. So, on our dashboard if our only
                SLO is let’s say latency < 200ms, then we must provide all the things that impact latency and latency
                itself. Providing chronological data to see trends and predict a breach in SLO is very important as well.
                Dashboards are meant to be a place where solutions can be found or where the solution can be located.
                Sometimes less is more on dashboards as well. Do not overpopulate your dashboards as it can confuse the viewer in what directions to look.
             """)
    
with auditing:
    st.write("""
            Recording all actions in production should be done. Anything done to production should be
            audited as in case there is a breach in the systems or change implemented that was not approved. This isn't to go back
             and blame individuals for doing a change in production without approval (however this is frowned upon), it is to be able to
             know what changes were made as in case there is an incident, we would know what could have caused it.
             """)
    
with versionControl:
    st.write("""
                Imagine that all your alerting, dashboards, and collection of metrics/logs/traces were managed through an Infrastructure as Code (IaC) or Configuration as Code (CaC) and all
                that code was managed on a version control such as Git. This would allow a change log, standarization, and easier management of monitoring for your platform. For cloud providers,
                their dashboards typically consist of being in JSON, so you can mantain the dashboard on Git as a JSON, where any changes to it would be documented. The real benefit of doing this
                is documentation and centrailization of managing monitoring. Instead of having to scour through your observability platform or cloud provider to manage alerts through multiple accounts, you
                could do it all through Git instead. This helps you know what you have, what you are monitoring, and see any changes.
             """)



