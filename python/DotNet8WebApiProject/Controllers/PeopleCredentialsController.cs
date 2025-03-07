using Microsoft.AspNetCore.Mvc;
using DotNet8WebApiProject.Models;

namespace DotNet8WebApiProject.Controllers;

[ApiController]
[Route("api/[controller]")]
public class PeopleCredentialsController : ControllerBase
{
    private static readonly List<PersonCredential> Credentials = new();

    [HttpGet("{personId}")]
    public ActionResult<PersonCredential> GetCredential(string personId)
    {
        var credential = Credentials.FirstOrDefault(c => c.PersonId == personId);
        if (credential == null) return NotFound();
        return Ok(credential);
    }

    [HttpGet]
    public ActionResult<List<PersonCredential>> GetAllCredentials()
    {
        return Ok(Credentials);
    }

    [HttpPost]
    public IActionResult AddCredential([FromBody] PersonCredential credential)
    {
        if (Credentials.Any(c => c.PersonId == credential.PersonId))
            return Conflict("Credential with the same PersonId already exists.");

        Credentials.Add(credential);
        return CreatedAtAction(nameof(GetCredential), new { personId = credential.PersonId }, credential);
    }

    [HttpPut]
    public IActionResult UpdateCredential([FromBody] PersonCredential credential)
    {
        var existingCredential = Credentials.FirstOrDefault(c => c.PersonId == credential.PersonId);
        if (existingCredential == null) return NotFound();

        existingCredential.Username = credential.Username;
        existingCredential.HashedPassword = credential.HashedPassword;
        existingCredential.CreatedAt = credential.CreatedAt;

        return NoContent();
    }

    [HttpDelete("{personId}")]
    public IActionResult DeleteCredential(string personId)
    {
        var credential = Credentials.FirstOrDefault(c => c.PersonId == personId);
        if (credential == null) return NotFound();

        Credentials.Remove(credential);
        return NoContent();
    }
}