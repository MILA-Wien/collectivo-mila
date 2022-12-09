<#import "template.ftl" as layout>
<@layout.registrationLayout displayMessage=false; section>
    <#if section = "header">
        Datenverarbeitung
    <#elseif section = "form">
    <div id="kc-terms-text">
        Ich erkläre mich ausdrücklich einverstanden, dass meine personenbezogenen Daten für Zwecke der Mitgliedschaft gem. GenG verarbeitet werden. Weitere Infos unter: 
        <a href="https://www.mila.wien/de/datenschutzerklaerung/" target="_blank">
            https://www.mila.wien/de/datenschutzerklaerung/
        </a>
    </div>
    <form class="form-actions" action="${url.loginAction}" method="POST">
        <input class="${properties.kcButtonClass!} ${properties.kcButtonPrimaryClass!} ${properties.kcButtonLargeClass!}" name="accept" id="kc-accept" type="submit" value="${msg("doAccept")}"/>
        <input class="${properties.kcButtonClass!} ${properties.kcButtonDefaultClass!} ${properties.kcButtonLargeClass!}" name="cancel" id="kc-decline" type="submit" value="${msg("doDecline")}"/>
    </form>
    <div class="clearfix"></div>
    </#if>
</@layout.registrationLayout>
