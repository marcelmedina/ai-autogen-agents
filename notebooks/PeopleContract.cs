using System;
using System.Collections.Generic;
using System.Runtime.Serialization;
using System.ServiceModel;

[ServiceContract]
public interface IPeopleCredentialsService
{
    [OperationContract]
    PersonCredential GetCredential(string personId);

    [OperationContract]
    List<PersonCredential> GetAllCredentials();

    [OperationContract]
    void AddCredential(PersonCredential credential);

    [OperationContract]
    void UpdateCredential(PersonCredential credential);

    [OperationContract]
    void DeleteCredential(string personId);
}

[DataContract]
public class PersonCredential
{
    [DataMember]
    public string PersonId { get; set; }
    
    [DataMember]
    public string Username { get; set; }
    
    [DataMember]
    public string HashedPassword { get; set; }
    
    [DataMember]
    public DateTime CreatedAt { get; set; }
}