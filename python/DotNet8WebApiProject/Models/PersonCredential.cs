namespace DotNet8WebApiProject.Models;

public class PersonCredential
{
    public string PersonId { get; set; } = "";
    public string Username { get; set; } = "";
    public string HashedPassword { get; set; } = "";
    public DateTime CreatedAt { get; set; }
}